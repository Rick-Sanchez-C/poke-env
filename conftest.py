


@fixture
def example_doubles_request():
    with open(os.path.join(FIXTURE_DIR, "example_doubles_request.json")) as f:
        return orjson.loads(f.read())
