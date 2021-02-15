# Configuring the taky Data Package Server

The data package server hosts information uploaded by the clients.

The work on this is very preliminary, and does not yet mirror the full
complexity of a TAK Server. Notably, I haven't figured out how to setup SSL
properly, and the Android client rejects the server (on searching).

## Step 1. Create the Necessary Directories

First, create a directory to store data packages. I like `/var/taky/dp-user`,
so I'll create it there, along with the meta directory. Make sure that
whichever user is running the daemons has write access to this directory!

```bash
$ mkdir -p /var/taky/dp-user/meta
```

## Step 2. Configure taky

Open up your `taky.conf` file in your favorite editor. We'll be editing the
`[dp_server]` section. This is pretty straightforward!

```
[dp_server]
upload_path=/var/taky/dp-user
```

## Step 3. Run the Data Package Server

There are a few ways to run flask applications. My preferred method is with
`gunicorn`. (The self hosting flask app is a little flakey when run in
threaded mode.)

```bash
$ gunicorn taky.dps -b 0.0.0.0:8080
```

If you want to use SSL (though it's broken), run

```bash
$ gunicorn taky.dps -b 0.0.0.0:8443 \
           --ca-certs /etc/taky/ssl/ca.crt \
           --certfile /etc/taky/ssl/server.crt \
           --keyfile /etc/taky/ssl/server.key
```

## Future Work

 * Why is the SSL certificate being rejected?
 * Automate running the data package server with gunicorn?
 * Systemd scripts?
 * Test using the DPS as a broker when devices are not on a local net