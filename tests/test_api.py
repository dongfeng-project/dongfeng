from rest_framework.reverse import reverse


def test_reverse():
    assert reverse(viewname="worker-monitor-log-list").endswith("worker-monitor-log/")
