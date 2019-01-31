from bioinformatics.janis_bioinformatics.tools import HTSLib_1_2_1
from bioinformatics.janis_bioinformatics.tools import TabixBase


class Tabix_1_2_1(HTSLib_1_2_1, TabixBase):
    pass


if __name__ == "__main__":
    print(Tabix_1_2_1().help())