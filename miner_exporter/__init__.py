from miner_exporter.cli import cli
import miner_exporter.subscribers.main
from miner_exporter.config.events_emitter import emitter
import traceback


def main():
    try:
        cli()
    except SystemExit:
        pass
    except BaseException as error:
        emitter.emit("logger.error", msg=repr(error))
        emitter.emit("logger.error", msg=traceback.print_exc().__str__())

    emitter.emit("logger.debug", msg="finished running cli.")


if __name__ == "__main__":
    main()
