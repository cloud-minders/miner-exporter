from miner_exporter.controllers import exporter_controller as controller
import click


@click.command()
@click.option(
    "--mode",
    "-m",
    type=click.Choice(
        ["server", "textfile", "pushgateway", "stdout"], case_sensitive=False
    ),
    default="server",
    show_default=True,
)
@click.option(
    "--textfile",
    "-tf",
    default="/var/lib/node_exporter/textfile_collector/gpu_exporter.prom",
    show_default=True,
    help="textfile location",
)
@click.option(
    "--port",
    "-p",
    default=9235,
    show_default=True,
    help="server port",
)
@click.option(
    "--push-url",
    "-pu",
    default="localhost:9091",
    show_default=True,
    help="pushgateway url",
)
@click.option(
    "--push-user",
    help="pushgateway username",
)
@click.option(
    "--push-pass",
    help="pushgateway password",
)
@click.option(
    "--push-job-id",
    help="pushgateway suffix for job name",
)
@click.option(
    "--interval",
    "-i",
    default=60,
    help="Interval in seconds for scraping metrics",
)
@click.option("--xmrig-url", help="The xmrig API address")
@click.option("--trex-url", help="The t-rex API address")
@click.option("--label", "-l", type=(str, str), multiple=True)
def exporter(
    mode,
    textfile,
    port,
    push_url,
    push_user,
    push_pass,
    push_job_id,
    interval,
    xmrig_url,
    trex_url,
    label,
):
    """Run exporter"""
    controller.start_exporter(
        interval=interval,
        push_url=push_url,
        push_pass=push_pass,
        push_job_id=push_job_id,
        server_port=port,
        textfile_path=textfile,
        mode=mode,
        push_user=push_user,
        trex_url=trex_url,
        xmrig_url=xmrig_url,
        custom_labels=label,
    )
