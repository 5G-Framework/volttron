import pytest
from volttrontesting.fixtures.volttron_platform_fixtures import volttron_instance_web

try:
    SKIP_DOCKER = False
    from volttrontesting.fixtures.docker_wrapper import create_container
except ImportError:
    SKIP_DOCKER = True


def test_web_setup_properly(volttron_instance_web):
    instance = volttron_instance_web

    assert instance.is_running()
    assert instance.bind_web_address == instance.volttron_central_address


@pytest.mark.skipif(SKIP_DOCKER, reason="No docker available in api (install pip install docker) for availability")
def test_docker_wrapper():
    with create_container("mysql") as container:
        print(container.status)
        print(container.logs())


@pytest.mark.skipif(SKIP_DOCKER, reason="No docker available in api (install pip install docker) for availability")
def test_docker_run_crate_latest():
    with create_container("crate", {"4200/tcp": 4200}) as container:
        assert container.status == 'running'

