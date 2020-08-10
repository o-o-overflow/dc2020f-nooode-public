.PHONY: public

public:
	tar cvzf ../public-nooode.tar.gz app.js bin package.json routes public views config.json node_modules
	cp ../public-nooode.tar.gz ../../patches/original-nooode.tar.gz.accepted

watch:
	echo Watching for changes...
	fswatch -e *.png -o . | xargs -n1 -I{} make debug && make watch

debug:
	-pkill npm
	DEBUG=express:*  npm start &

cleanup:
	-docker rm $(docker ps -a -f status=exited -q)
	-docker images -a | grep "test-nooode" | awk '{print $3}' | xargs docker rmi
	docker build -t test-nooode .
	docker run -p 4017:4017 test-nooode

benchmark:
	ulimit -n 10000
	ab -n 10000 -c 20000 http://localhost:4017/