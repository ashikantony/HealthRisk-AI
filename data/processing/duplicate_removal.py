class DuplicateRemover:

    @staticmethod
    def remove_duplicates(df):

        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        removed = before - after

        print(
            f"Duplicates Removed: {removed}"
        )

        return df