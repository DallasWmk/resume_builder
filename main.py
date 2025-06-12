import inquirer
import sys
import pypdf


def get_contact_info():
    """
    get_contact_info is used to obtain the name,
    phone number, and email of the user for the
    header of the resume.
    Args:
        None
    Output:
        None | dict(str, str)
    """
    questions = [
        inquirer.Text("name", message="What is your frist name?"),
        inquirer.Text("surname", message="What is your surname?"),
        inquirer.Text(
            "phone", message="What phone number would you like to be contacted at?"
        ),
        inquirer.Text("email", message="What email would you like to be contacted at?"),
    ]

    answers = inquirer.prompt(questions)
    return answers


def has_links() -> bool:
    """
    has_links() asks if the user if they would like
    to provide links such as personal websites,
    LinkedIn, Github, etc.
    Args:
        None
    Output:
        Bool
    """
    links = [
        inquirer.Confirm("links", message="Do you want to provide links?", default=True)
    ]
    answer = inquirer.prompt(links)
    if answer is not None:
        return answer["links"]
    return False


def get_links(has_links):
    """
    get_links() asks if the user to provide word, and links
    they would like to embed within the words
    Args:
        None
    Output:
        dict[str,str]
    """
    user_links = {}  # dictionary of words and what they should be linked to
    while has_links:
        links = [
            inquirer.Text("text", message="what text should be used for display?"),
            inquirer.Text(
                "link", message="what link would you like to embed in the text?"
            ),
        ]
        link = inquirer.prompt(links)
        if link is None:
            print("Prompt cancelled by user.")
            sys.exit(0)
        else:
            print(f"links: {links}")
            user_links[link["text"]] = link["link"]
        more = [inquirer.Confirm("continue", message="add another link?", default=True)]
        has_more = inquirer.prompt(more)
        if has_more:
            has_links = has_more["continue"]
        else:
            has_links = False


def get_summary():
    """
    get_summary() asks if the user to provide a
    professional summary for their resume
    Args:
        None
    Output:
        str
    """
    questions = [
        inquirer.Editor("summary", message="Provide your professional summary:")
    ]
    answers = inquirer.prompt(questions)
    if answers is None:
        print("user cancelled prompt")
        sys.exit()
    return answers["summary"]


def main():
    print("Hello from resume-builder!")
    print("Lets get started building your resume")

    contact_info = get_contact_info()

    links: dict[str, str] = {}
    links_to_add = has_links()
    if links_to_add is not None:
        links = get_links(links_to_add)

    summary = get_summary()

    print(
        f"contact_info:\nname: {contact_info['name']+' '+contact_info['surname']}\nemail: {contact_info['email']}\nphone: {contact_info['phone']}\nsummary: {summary}"
    )


if __name__ == "__main__":
    main()
