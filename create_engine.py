user = "admin"
pwd = "dlwndwo2"
host = "tutorial.crotgxtzxtks.ap-northeast-2.rds.amazonaws.com"
port = 3306
db_url = f'mysql+pymysql://{user}:{quote(pwd)}@{host}:{port}/information?charset=utf8mb4'



ENGINE = create_engine(db_url, echo=True)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()
Base.metadata.create_all(bind=ENGINE)
