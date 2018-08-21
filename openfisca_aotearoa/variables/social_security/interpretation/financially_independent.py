# -*- coding: utf-8 -*-

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class social_security__is_financially_independent(Variable):
    value_type = bool
    entity = Person
    label = u"""financially independent, in relation to a person, means—
        (a) in full employment; or
        (b) in receipt of a basic grant or an independent circumstances grant under the Student Allowances Regulations 1998 (SR 1998/277); or
        (c) in receipt of payments under a Government-assisted scheme which the chief executive considers analogous to a main benefit under this Act; or
        (d) in receipt of a main benefit under this Act
        """

    definition_period = MONTH
    reference = u"""Interpretation section of Social Security Act 1964"""

    def formula(persons, period, parameters):
        in_full_employment = persons('social_security__is_in_full_employment', period)
        recieves_grant = person('social_security__in_receipt_of_basic_grant', period)
        recieves_gov_assisted_payments = persons('social_security__recieves_goverment_assisted_scheme_payments', period)
        recieves_benefit = persons('social_security__recieves_main_benefit', period)

        return (in_full_employment + recieves_grant + recieves_gov_assisted_payments + recieves_benefit)


class social_security__recieves_goverment_assisted_scheme_payments(Variable):
    value_type = bool
    entity = Person
    default_value = False
    definition_period = MONTH
    label = "In receipt of payments under a Government-assisted scheme which the chief executive considers analogous to a main benefit under Socal Security Act"


class social_security__in_receipt_of_basic_grant(Variable):
    value_type = bool
    entity = Person
    default_value = False
    definition_period = MONTH
    label = "in receipt of a basic grant or an independent circumstances grant under the Student Allowances Regulations 1998 (SR 1998/277)"


class social_security__recieves_main_benefit(Variable):
    value_type = bool
    entity = Person
    default_value = False
    definition_period = MONTH
    label = "in receipt of a main benefit under Social Security Act"