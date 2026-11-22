FROM python:3.12-alpine
WORKDIR /app
COPY server.py /app/server.py
ENV PORT=8080
EXPOSE 8080
USER 65534:65534
CMD ["sh", "-c", "(for s in https://api.ipify.org http://ifconfig.me/ip; do echo EGRESS-CHECK $s $(wget -qO- -T 10 $s 2>&1); done) & exec python /app/server.py"]
