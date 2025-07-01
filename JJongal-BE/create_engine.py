user = "admin"
pwd = "dlwndwo2"
host = "https://nest-database.cdg64u0o8ii4.ap-southeast-2.rds.amazonaws.com/"
port = 3306
db_url = f'mysql+pymysql://{user}:{quote(locallocal)}@{host}:{3306}/information?charset=utf8mb4'



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
