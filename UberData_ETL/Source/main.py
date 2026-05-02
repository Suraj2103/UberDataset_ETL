from .extract import Extract
from .transform import Transform
from .load import Load

def run_pipeline():

    extractor = Extract("data/uber.csv")
    transformer = Transform()
    loader = Load()

    df = extractor.run()
    df = transformer.run(df)
    loader.run(df)

if __name__ == "__main__":
    run_pipeline()