run: 
	bundle exec jekyll serve

setup:
	bundle config set --local path 'vendor/bundle'
	bundle install

clean:
	bundle exec jekyll clean
