class PullRequest:
    """Represents a GitHub Pull Request."""

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def is_valid(self) -> bool:
        """Validate pull request details."""
        return (
            self.title.strip() != ""
            and len(self.title) >= 5
            and self.author.strip() != ""
        )

    def get_details(self) -> str:
        """Return PR details."""
        return f"Pull Request: {self.title} " f"created by {self.author}"


def main():
    """Application entry point."""

    pull_request = PullRequest(
        title="Added Power Automate Notification", author="Spoorthi"
    )

    if pull_request.is_valid():
        print(pull_request.get_details())
    else:
        print("Invalid Pull Request")


if __name__ == "__main__":
    main()
