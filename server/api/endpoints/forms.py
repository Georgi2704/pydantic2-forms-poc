# Copyright 2019-2023 SURF.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from http import HTTPStatus
from typing import Any

from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from pydantic_forms.core import list_forms
from pydantic_forms.core.asynchronous import start_form

from server.forms.examples import minimal_example_form, register_form
# from oauth2_lib.fastapi import OIDCUserModel
# from orchestrator.security import oidc_user

router = APIRouter()


def register_forms():
    pass

@router.get("/")
def get_forms() -> list[str]:
    """Retrieve all forms.

    Returns:
        Form titles

    """
    register_forms()
    return list_forms()


@router.post("/{form_key}", status_code=HTTPStatus.CREATED)
async def new_form(
    form_key: str,
    json_data: list[dict[str, Any]],
) -> dict[str, Any]:
    # Todo: determine what to do with user?
    return await start_form(form_key, user_inputs=json_data, user="Just a user")
