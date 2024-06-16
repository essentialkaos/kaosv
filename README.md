<p align="center"><a href="#readme"><img src=".github/images/card.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/kaosv/ci"><img src="https://kaos.sh/w/kaosv/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src=".github/images/license.svg"/></a>
</p>

<p align="center"><a href="#documentation">Documentation</a> • <a href="#examples">Examples</a> • <a href="#common-mistakes">Common mistakes</a> • <a href="#ci-status">CI Status</a> • <a href="#license">License</a></p>

<br/>

`kaosv` is bash lib for SysV init scripts.

### Documentation

KAOSv contain inline documentation in shdoc format.

Documentation for latest version can be found [here](https://docs.kaos.st/kaosv/latest/). Also you can use [SHDoc](https://github.com/essentialkaos/shdoc) utility for viewing inline docs in your console.

### Examples

* [memcached](https://github.com/essentialkaos/kaos-repo/blob/master/specs/memcached/SOURCES/memcached.init)
* [pgbouncer](https://github.com/essentialkaos/kaos-repo/blob/master/specs/pgbouncer/SOURCES/pgbouncer.init)
* [postgresql](https://github.com/essentialkaos/kaos-repo/blob/master/specs/postgresql-11/SOURCES/postgresql.init)
* [redis](https://github.com/essentialkaos/kaos-repo/blob/master/specs/redis/SOURCES/redis.init)
* [salt](https://github.com/essentialkaos/kaos-repo/blob/master/specs/salt/SOURCES/salt-master.init)
* [webkaos](https://github.com/essentialkaos/webkaos/blob/master/SOURCES/webkaos.init)

### Common mistakes

**Checking the system environment before executing `kv.go`**

You should define a pre-start handler with [disabled output redirect](https://docs.kaos.st/kaosv/2.15.3/#491) and perform system check in this handler ([example](https://github.com/essentialkaos/kaos-repo/blob/master/specs/pgbouncer/SOURCES/pgbouncer.init#L86)).


**The script doesn't run application and return a non-zero exit code**

All handlers must always return action status code (`ACTION_OK`, `ACTION_ERROR`, `ACTION_FORCED`) otherwise it can be exit code from the last command performed in this handler.

### CI Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/kaosv/ci.svg?branch=master)](https://kaos.sh/w/kaosv/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/kaosv/ci.svg?branch=master)](https://kaos.sh/w/kaosv/ci?query=branch:develop) |

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
