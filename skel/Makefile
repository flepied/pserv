TOPDIR = /var/lib/adminkit

install:
	set -x; for d in files roles adminkit.conf.d; do mkdir -p $(DESTDIR)$(TOPDIR)/$$d; cp -r $$d/ $(DESTDIR)$(TOPDIR)/; done
