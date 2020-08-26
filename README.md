# TPMI_searchManagement

![](https://img.shields.io/static/v1?label=python&message=3.7&color=yellow)
![](https://img.shields.io/static/v1?label=mysql&message=8.X&color=red)
![](https://img.shields.io/static/v1?label=Django&message=3.0.3&color=green)
![](https://img.shields.io/static/v1?label=Docker&message=3.0.3&color=blue)

***This system can supply for search database***


<a href=""><img src="img/main.png" title="FVCproductions" alt="FVCproductions"></a>



## Table of Contents

- [Install](#install)
- [Introduction](#introduction)
- [Contributors](#contributors)
- [Sponsors](#sponsors)
- [Community](#community)
- [Establishing connections](#establishing-connections)
- [Connection options](#connection-options)
  - [SSL options](#ssl-options)
  - [Connection flags](#connection-flags)
- [Terminating connections](#terminating-connections)
- [Pooling connections](#pooling-connections)
- [Pool options](#pool-options)
- [Pool events](#pool-events)
  - [acquire](#acquire)
  - [connection](#connection)
  - [enqueue](#enqueue)
  - [release](#release)
- [Closing all the connections in a pool](#closing-all-the-connections-in-a-pool)
- [PoolCluster](#poolcluster)
  - [PoolCluster options](#poolcluster-options)
- [Switching users and altering connection state](#switching-users-and-altering-connection-state)
- [Server disconnects](#server-disconnects)
- [Performing queries](#performing-queries)
- [Escaping query values](#escaping-query-values)
- [Escaping query identifiers](#escaping-query-identifiers)
  - [Preparing Queries](#preparing-queries)
  - [Custom format](#custom-format)
- [Getting the id of an inserted row](#getting-the-id-of-an-inserted-row)
- [Getting the number of affected rows](#getting-the-number-of-affected-rows)
- [Getting the number of changed rows](#getting-the-number-of-changed-rows)
- [Getting the connection ID](#getting-the-connection-id)
- [Executing queries in parallel](#executing-queries-in-parallel)
- [Streaming query rows](#streaming-query-rows)
  - [Piping results with Streams](#piping-results-with-streams)
- [Multiple statement queries](#multiple-statement-queries)
- [Stored procedures](#stored-procedures)
- [Joins with overlapping column names](#joins-with-overlapping-column-names)
- [Transactions](#transactions)
- [Ping](#ping)
- [Timeouts](#timeouts)
- [Error handling](#error-handling)
- [Exception Safety](#exception-safety)
- [Type casting](#type-casting)
  - [Number](#number)
  - [Date](#date)
  - [Buffer](#buffer)
  - [String](#string)
  - [Custom type casting](#custom-type-casting)
- [Debugging and reporting problems](#debugging-and-reporting-problems)
- [Security issues](#security-issues)
- [Contributing](#contributing)
- [Running tests](#running-tests)
  - [Running unit tests](#running-unit-tests)
  - [Running integration tests](#running-integration-tests)
- [Todo](#todo)

## Install

This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/).

Before installing, [download and install Node.js](https://nodejs.org/en/download/).
Node.js 0.6 or higher is required.

Installation is done using the
[`npm install` command](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):

```sh
$ npm install mysql
```

For information about the previous 0.9.x releases, visit the [v0.9 branch][].

Sometimes I may also ask you to install the latest version from Github to check
if a bugfix is working. In this case, please do:

```sh
$ npm install mysqljs/mysql
```

[v0.9 branch]: https://github.com/mysqljs/mysql/tree/v0.9

