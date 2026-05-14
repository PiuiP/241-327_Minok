FROM nginx:alpine

# Удаляем стандартный конфиг
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш шаблон
COPY templates/default.conf.template /etc/nginx/templates/default.conf.template