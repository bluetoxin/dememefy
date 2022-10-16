from argparse import ArgumentParser

from dememefy import posts
from dememefy.image import Demotivator

SERVICES = {
    "reddit": (posts.RedditPosts, ["username", "password", "client_id", "token"], ["thread"]),
}


def _parse_args():
    parser = ArgumentParser(
        prog="dememefy", description="Make media fun again")
    parser.add_argument(
        "--service", "-s",
        dest="service",
        type=str,
        choices=SERVICES.keys(),
        help="Target Service")
    parser.add_argument(
        "--thread", "-t",
        dest="thread",
        type=str,
        help="Thread contains posts for parsing")
    parser.add_argument(
        "--username", "-u",
        dest="username",
        type=str,
        help="Username for destination service (if needed by service).")
    parser.add_argument(
        "--password", "-p",
        dest="password",
        type=str,
        help="Password for destination service (if needed by service).")
    parser.add_argument(
        "--client-id", "-ci",
        dest="client_id",
        type=str,
        help="Client ID for destination service (if needed by service).")
    parser.add_argument(
        "--secret-token", "-st",
        dest="token",
        type=str,
        help="Token for destination service (if needed by service).")
    return parser.parse_args()


def main():
    args = _parse_args()
    service_name, credentials, params = SERVICES[args.service]

    kwargs = {}
    for arg_name in [*credentials, *params]:
        arg_value = getattr(args, arg_name)
        if arg_value is not None:
            kwargs[arg_name] = arg_value
        elif arg_name in credentials:
            raise ValueError(f"{arg_name} is missing")

    service = service_name(**kwargs)
    text, picture = service.get_post()
    demotivator = Demotivator(image=picture, text=text, x_start=75, y_start=45)
    picture = demotivator.create()
    picture.show()
