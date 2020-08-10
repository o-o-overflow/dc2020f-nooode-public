FROM keymetrics/pm2:12-slim

RUN apt-get update && apt-get install -y procps

RUN useradd -s /bin/bash -m oooser
RUN mkdir -p /service
COPY --chown=oooser:oooser public-nooode.tar.gz /
COPY --chown=oooser:oooser patch.sh /
# COPY --chown=oooser:oooser src /service
RUN chmod 755 /patch.sh
RUN /patch.sh

WORKDIR /service/

# Install app dependencies
ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install --production
RUN npm rebuild node-sass

# The flagbot will periodically echo the flag > this file (flag_path in info.yaml)
RUN touch /flag && chmod 644 /flag && echo "000AAAA" > /flag
RUN chown oooser:oooser -R /service
RUN chmod 0500 -R /service


# Expose the listening port of your app
ENV PORT 4017
EXPOSE 4017

CMD /patch.sh && pm2-runtime bin/www -u oooser
