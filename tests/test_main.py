import random

import pytest
from faker import Faker

from . import utils as u

fake = Faker()


@pytest.mark.parametrize(
    "zip_code,project_type,equipment,hvac,age,property_type,authorized",
    [
        (
            "10001",
            "Replacement/installation",
            "Central heating/furnace",
            "Gas",
            "Less than 5 years",
            "Detached, semi-detached, row house",
            "Yes",
        ),
        (
            "10001",
            "Replacement/installation",
            "Water heater",
            "Electricity",
            "Less than 5 years",
            "Detached, semi-detached, row house",
            "Yes",
        ),
        (
            "10001",
            "Replacement/installation",
            "Boiler/radiator",
            "Oil",
            "Less than 5 years",
            "Detached, semi-detached, row house",
            "Yes",
        ),
    ],
)
def test_create_project(
    driver,
    open_home_page,
    teardown,
    zip_code,
    project_type,
    equipment,
    hvac,
    age,
    property_type,
    authorized,
):
    msg = u.create_project(
        driver,
        zip_code=zip_code,
        project_type=project_type,
        equipment=equipment,
        hvac=hvac,
        age=age,
        property_type=property_type,
        house_area=random.randint(1000, 2000),
        authorized=authorized,
        name=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
    )
    assert (
        msg
        == "We're sorry, but we couldn't find any contractors\nmatching your project requirements."
    ), f"Expected: 'Thank you'. Actual: '{msg}'"
