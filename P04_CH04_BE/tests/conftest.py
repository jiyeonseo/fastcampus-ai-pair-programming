import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import models
from app.db.session import Base

@pytest.fixture(scope="function")
def db_session():
    # 테스트용 데이터베이스 엔진 생성
    engine = create_engine("sqlite:///./test.db")
    Base.metadata.create_all(bind=engine)  # 테스트용 데이터베이스 스키마 생성
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)  # 테스트 후 데이터베이스 정리
