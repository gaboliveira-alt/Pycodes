from typing import Literal, TypedDict

from utils import cyan_print, green_print, red_print, sep_print


class ResponseSucess(TypedDict):
    status: Literal["ok"]
    data: str


class ResponseError(TypedDict):
    status: Literal["error"]
    message: str


type Response = ResponseSucess | ResponseError


def handle_response(response: Response):
    match response["status"]:
        case "ok":
            green_print("RESPONSE OK!", response["data"])
            return
        case "error":
            red_print("ERROR", response["message"])
            return

    red_print("💥 I can't handle this response")


if __name__ == "__main__":
    sep_print()

    response_success: ResponseSucess = {"status": "ok", "data": "Here is your result"}
    handle_response(response_success)
    cyan_print()
    sep_print()

    response_error: ResponseError = {"status": "error", "message": "BadRequest"}
    handle_response(response_error)
    cyan_print()
    sep_print()

    wrong_response = {"status": "any"}
    handle_response(wrong_response)
    cyan_print()
    sep_print()
