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

from pydantic import EmailStr
from pydantic_forms.core import FormPage, ReadOnlyField, register_form
from pydantic_forms.types import FormGeneratorAsync, State
from pydantic_forms.validators import Choice, LongText


class ChoiceType(Choice):
    A = "Option A"
    B = "Option B"
    C = "Option C"


async def minimal_example_form(current_state: State) -> FormGeneratorAsync:
    """Form with only string fields."""

    class Form(FormPage):
        class Config:
            title = "A test for the form module"

        first_name: str
        last_name: str = ReadOnlyField("Kruger")
        text: LongText
        choice: ChoiceType
        email: EmailStr | None
        maybe_a_number: int | None

    form = yield Form

    class Form2(FormPage):
        class Config:
            title = "Testing the wizard"

        age: int

    form2 = yield Form2

    yield {**form.dict(), **form2.dict()}


register_form("minimal_example_form", minimal_example_form)
