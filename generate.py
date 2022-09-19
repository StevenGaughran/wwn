from data.terrain_feature_detail import TerrainFeatureDetail
from data.nation_detail import NationDetail
from data.population_features import PopulationDetail
from data.society_detail import SocietyDetail
from data.government_ruler_detail import RulerDetail
from data.government_detail import GovernmentDetail
from data.history_detail import HistoryDetail


def nation_generation():
    tfd = TerrainFeatureDetail()
    nd = NationDetail()
    pd = PopulationDetail()
    sd = SocietyDetail()
    rd = RulerDetail()
    gd = GovernmentDetail()
    hd = HistoryDetail()
    deets = (tfd.generate(), nd.generate(), pd.generate(), sd.generate(), rd.generate(), gd.generate(), hd.generate())
    with open("wwn_nation_generation.txt", "w") as file:
        for i in deets:
            file.write(i)


nation_generation()
