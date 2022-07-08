# miner_exporter

Collect data about miners and exposes them for Prometheus

## Table of Contents

- [miner_exporter](#miner_exporter)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
    - [xmrig](#xmrig)
      - [Metrics Chart](#metrics-chart)
    - [t-rex](#t-rex)
      - [Metrics Chart](#metrics-chart-1)
  - [Maintainers](#maintainers)
  - [License](#license)

## Usage
> 💡  [More information on poetry](https://python-poetry.org/docs/)


```sh
# install dependencies
$ poetry install

# shell into project
$ poetry shell
```

```sh
$ python main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  exporter  Run exporter

```

```sh
$ python main.py exporter --help
Usage: main.py exporter [OPTIONS]

  Run exporter

Options:
  -p, --port INTEGER  The listening port  [default: 9189]
  --bind TEXT         The bind address  [default: 127.0.0.1]
  --xmrig-url TEXT    The xmrig API address
  --trex-url TEXT     The t-rex API address
  --help              Show this message and exit.

```

Exposes metrics API on 127.0.0.1:9189 by default

```sh
$ python main.py exporter --xmrig-url http://127.0.0.1:8080/1/summary --trex-url http://127.0.0.1:4067/summary
```

### xmrig
> 💡 [More information about what data the xmrig miner API exposes](https://github.com/xmrig/xmrig/blob/master/doc/api/1/summary.json)

#### Metrics Chart
| Metric                   | Description        | Type    |
| ------------------------ | ------------------ | ------- |
| xmrig_hashrate#          | Overall Hashrate   | Gauge   |
| xmrig_diff_current       | Current Difficulty | Gauge   |
| xmrig_shares_good        | Good Shares        | Counter |
| xmrig_shares_total       | Total Shares       | Counter |
| xmrig_avg_time           | Average Time       | Gauge   |
| xmrig_hashes_total       | Total Hashes       | Counter |
| xmrig_best               | Best               | Gauge   |
| xmrig_errors             | Count of errors    | Counter |
| xmrig_connection_uptime  | Connection uptime  | Gauge   |
| xmrig_connection_ping    | Connection ping    | Gauge   |
| xmrig_connection_failure | Connection failure | Counter |

### t-rex
> 💡 [More information about t-rex miner API](https://github.com/trexminer/T-Rex/wiki/API)

#### Metrics Chart
| Metric              | Description                | Type  |
| ------------------- | -------------------------- | ----- |
| gpu_hashrate        | GPU Hashrate               | Gauge |
| hashrate_total      | Overall Hashrate           | Gauge |
| hashrate_day        | Hashrate in day            | Gauge |
| hashrate_hour       | Hashrate in hour           | Gauge |
| hashrate_minute     | Hashrate in minute         | Gauge |
| gpu_total           | Total gpus                 | Gauge |
| sharerate           | Sharerate                  | Gauge |
| sharerate_average   | Average Sharerate          | Gauge |
| accepted_count      | Accepted share count       | Gauge |
| rejected_count      | Rejected share count       | Gauge |
| pool_last_submit_ts | Pool last sumbit timestamp | Gauge |
| pool_ping           | Pool ping                  | Gauge |

## Maintainers

[@mezerotm](https://github.com/mezerotm)

## License

© 2022 Cloud Minders