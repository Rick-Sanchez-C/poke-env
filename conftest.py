# -*- coding: utf-

@fixture
def packed_format_teams(raw_team_data):
    data = {}
    for format_, team_list in raw_team_data.items():
        data[format_] = []

        for team_info in team_list:
            data[format_].append(team_info["packed-format"])
    return data


@fixture
def raw_team_data():
    with open(os.path.join(FIXTURE_DIR, "teams.json")) as f:
        return orjson.loads(f.read())


@fixture
def example_request():
    with open(os.path.join(FIXTURE_DIR, "example_request.json")) as f:
        return orjson.loads(f.read())


@fixture
def example_doubles_request():
    with open(os.path.join(FIXTURE_DIR, "example_doubles_request.json")) as f:
        return orjson.loads(f.read())
