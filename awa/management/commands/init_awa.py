from awa.settings import config
from logging import info, debug, getLogger, DEBUG, INFO

from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model

from apps.pages.models import Page

log = getLogger("django")
log.level = INFO


class Command(BaseCommand):
    help = "Run initialization/sanity checks for AWA"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("-c", "--clean", action="store_true")
        return super().add_arguments(parser)

    def handle(self, *args, **kwargs):
        self.admin = self.check_default_admin()
        self.fix_sites()

    def check_default_admin(self):
        self.stdout.write("checking if a default admin exists")
        UserClass = get_user_model()
        admin_user = config.admin_user or "admin"
        user, is_new = UserClass.objects.get_or_create(username=admin_user)
        if is_new:
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.set_password(config.admin_password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f"default admin {admin_user} was created")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f"existing user {config.admin_user} not modified")
            )
        return user

    def fix_sites(self):
        try:
            self.stdout.write("checking site configurations")

            project = config.project
            home_page = Page.objects.get_or_create(
                slug="index", defaults={
                    "title":"Home",
                    "created_by":self.admin,
                }
            )
            pnf = Page.objects.get_or_create(
                slug="404", defaults={
                    "title":"Page not found",
                    "created_by":self.admin,
                }
            )
            for domain in project.domains:
                site, site_is_new = Site.objects.get_or_create(
                    domain=domain.domain,
                    defaults={"name":project.slug}, 
                )
            self.stdout.write(self.style.SUCCESS("complete."))
        except CommandError as e:
            self.stderr.write(self.style.ERROR(e))
