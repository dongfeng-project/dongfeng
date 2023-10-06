# def test_block_subprocess():
#     start = time.time()
#     jobs = group([block_subprocess_task.s() for _ in range(10)])
#     result = jobs.apply_async()
#     result.get()
#     end = time.time()
#     print(f"finished in {int(end - start)}s")


# def test_nmap_detect_up_host():
#     from tasks.scout import nmap_detect_up_hosts
#
#     ips = "192.168.0.1-192.168.3.1"
#     t = nmap_detect_up_hosts.delay(ips)
#     result = t.get()
#     assert "192.168.2.1" in result.up_hosts
