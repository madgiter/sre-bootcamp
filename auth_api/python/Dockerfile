FROM python:3-alpine
ADD ./ /home
#RUN apt-get install pip3
RUN pip3 install flask
RUN pip3 install mysql-connector-python
#copy /home/new/jbshare/sre-bootcamp/auth_api/python/api.py /home/.
EXPOSE 8000
RUN ls -alr ./home
CMD ["python3", "./home/api.py"]
# Add your instructions to dockerize the application
# App must run on port 8000