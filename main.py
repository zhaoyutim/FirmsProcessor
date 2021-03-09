import yaml

from FirmsProcessor.FirmsProcessor import FirmsProcessor

with open("config/configuration.yml", "r", encoding="utf8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

if __name__=='__main__':
    locations = ['R92033', 'R91947']
    for location in locations:
        firmsProcessor = FirmsProcessor('Canada')
        firmsProcessor.firms_generation_from_csv_to_tiff(config.get(location).get('start'), config.get(location).get('end'), location)
        firmsProcessor.accumulation(location)