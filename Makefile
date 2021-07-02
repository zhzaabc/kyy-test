PYTHON_BASE_IMAGE_NAME=registry.cn-beijing.aliyuncs.com/kaoyaya-micro/python-base-image
EXAM_QUERY_IMAGE_NAME=registry.cn-beijing.aliyuncs.com/kaoyaya-micro/python-exam-query:v2.5
EXAM_QUERY_PROVINCE_IMAGE_NAME=registry.cn-beijing.aliyuncs.com/kaoyaya-micro/python-exam-query-province
GET_SCORE_IMAGE_NAME=registry.cn-beijing.aliyuncs.com/kaoyaya-micro/python-get-score
APPLY_EXAM_IMAGE_NAME=registry.cn-beijing.aliyuncs.com/kaoyaya-micro/python-apply-exam
GET_SCORE_ALL_IMAGE_NAME=registry.cn-beijing.aliyuncs.com/kaoyaya-micro/python-get-score-all

build-base-image:
	@docker build -t $(PYTHON_BASE_IMAGE_NAME) -f Dockerfile-base-image .

push-exam-query:
	@docker build -t $(EXAM_QUERY_IMAGE_NAME) -f Dockerfile-exam-query .
	@docker push $(EXAM_QUERY_IMAGE_NAME)

push-exam-query-province:
	@docker build -t $(EXAM_QUERY_PROVINCE_IMAGE_NAME) -f Dockerfile-exam-query-province .
	@docker push $(EXAM_QUERY_PROVINCE_IMAGE_NAME)

push-get-score:
	@docker build -t $(GET_SCORE_IMAGE_NAME) -f Dockerfile-get-score .
	@docker push $(GET_SCORE_IMAGE_NAME)

push-get-score-all:
	@docker build -t $(GET_SCORE_ALL_IMAGE_NAME) -f Dockerfile-get-score-all .
	@docker push $(GET_SCORE_ALL_IMAGE_NAME)

push-apply-exam:
	@docker build -t $(APPLY_EXAM_IMAGE_NAME) -f Dockerfile-apply-exam .
	@docker push $(APPLY_EXAM_IMAGE_NAME)
models:
	@sqlacodegen mysql+pymysql://root:kaoyayacom2017@test.server.kaoyaya.com:33006/sq_kaoyaya > models/base_models.py

freeze:
	@pip freeze > requirements.txt

