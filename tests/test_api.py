from rest_framework.reverse import reverse


def test_reverse():
    assert reverse(viewname="worker-monitor-log-list").endswith("worker-monitor-log/")
    assert reverse(viewname="worker-monitor-log-cleanup").endswith("worker-monitor-log-cleanup/")
