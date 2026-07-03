import re


class ICDExtractor:

    ICD_PATTERN = (
        r"\b[A-TV-Z][0-9]{2}"
        r"(?:\.[A-Z0-9]{1,4})?\b"
    )

    @classmethod
    def extract_codes(
        cls,
        text
    ):

        codes = re.findall(
            cls.ICD_PATTERN,
            text.upper()
        )

        return list(
            set(codes)
        )

    @classmethod
    def diagnosis_count(
        cls,
        text
    ):

        return len(
            cls.extract_codes(
                text
            )
        )