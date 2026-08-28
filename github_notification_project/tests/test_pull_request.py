from src.pull_request import PullRequest


def test_valid_pull_request():
    pull_request = PullRequest(
        "Added Notification Flow",
        "Spoorthi"
    )

    assert pull_request.is_valid() is True


def test_invalid_pull_request_title():
    pull_request = PullRequest(
        "",
        "Spoorthi"
    )

    assert pull_request.is_valid() is False


def test_invalid_pull_request_author():
    pull_request = PullRequest(
        "Added Notification Flow",
        ""
    )

    assert pull_request.is_valid() is False


def test_pull_request_details():
    pull_request = PullRequest(
        "Added Notification Flow",
        "Spoorthi"
    )

    expected = (
        "Pull Request: Added Notification Flow "
        "created by Spoorthi"
    )

    assert pull_request.get_details() == expected