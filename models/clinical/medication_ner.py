import re


class MedicationNER:

    COMMON_MEDICATIONS = {
        "metformin",
        "aspirin",
        "insulin",
        "warfarin",
        "atorvastatin",
        "lisinopril",
        "amoxicillin",
        "paracetamol",
        "ibuprofen",
        "omeprazole"
    }

    @classmethod
    def extract_medications(
        cls,
        text
    ):

        text = text.lower()

        medications = []

        for medication in (
            cls.COMMON_MEDICATIONS
        ):
            pattern = (
                r"\b"
                + medication
                + r"\b"
            )

            if re.search(
                pattern,
                text
            ):
                medications.append(
                    medication
                )

        return medications

    @classmethod
    def medication_count(
        cls,
        text
    ):

        return len(
            cls.extract_medications(
                text
            )
        )