from generate_data import main as generate
from build_database import main as build
from create_visuals import main as visuals
if __name__=='__main__': generate(); build(); visuals(); print('Pipeline completed successfully.')
