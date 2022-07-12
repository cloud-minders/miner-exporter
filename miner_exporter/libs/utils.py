from prometheus_client.core import (
    CounterMetricFamily,
    GaugeMetricFamily,
    InfoMetricFamily,
)
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def requests_retry_session(
    retries=7,
    back_off_factor=0.3,
    status_force_list=(500, 502, 504, 503),
    session=requests.Session(),
):
    session = session
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=back_off_factor,
        status_forcelist=status_force_list,
        method_whitelist=frozenset(["GET", "POST"]),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def make_metric(name, documentation, value, metric_type="counter", **labels):
    """
    It takes a metric name, documentation, value, and a dictionary of labels, and returns a metric
    object

    :param name: The name of the metric
    :param documentation: A string that will be used as the documentation for the metric
    :param value: The value of the metric
    :param metric_type: The type of metric. Can be one of: counter, gauge, summary, histogram, defaults
    to counter (optional)
    :return: A metric object
    """
    label_names = list(labels.keys())

    c = CounterMetricFamily

    if metric_type == "gauge":
        c = GaugeMetricFamily
    if metric_type == "info":
        c = InfoMetricFamily
    # elif metric_type == "summary":
    #     c = SummaryMetricFamily
    # elif metric_type == "histogram":
    #     c = HistogramMetricFamily

    metric = c(name, documentation or "No Documentation", labels=label_names)
    metric.add_metric([str(labels[k]) for k in label_names], value)

    return metric
