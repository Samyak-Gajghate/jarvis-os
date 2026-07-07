from backend.container.dependencies import container


def test_runtime_registered():
    runtime = container.resolve("runtime")

    assert runtime is not None