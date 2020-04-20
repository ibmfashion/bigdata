docker run -d --restart=unless-stopped \
-p 80:80 -p 443:443 \
-v /Users/getech/rancher/rancher2:/var/lib/rancher/ \
-v /Users/getech/rancher/rancher2/log/auditlog:/var/log/auditlog \
-e CATTLE_SYSTEM_CATALOG=bundled \
-e AUDIT_LEVEL=3 \
rancher/rancher:latest (或者rancher/rancher:latest)
