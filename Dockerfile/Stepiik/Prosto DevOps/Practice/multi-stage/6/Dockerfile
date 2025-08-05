FROM ruby:3.1 AS builder

RUN apt-get update -qq && \
    apt-get install -y nodejs npm build-essential libpq-dev && \
    npm install -g yarn && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV BUNDLE_PATH=/usr/local/bundle
COPY Gemfile Gemfile.lock ./
RUN bundle config set --local without 'development test' && \
    bundle install --jobs=4

COPY package.json yarn.lock ./
RUN yarn install

COPY . .
RUN SECRET_KEY_BASE=dummy RAILS_ENV=production bundle exec rails assets:precompile && \
    rm -rf tmp/cache node_modules app/javascript vendor/javascript


FROM ruby:3.1-slim

RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends libpq5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -r rails && useradd -r -g rails rails
USER rails


WORKDIR /app

COPY --from=builder /usr/local/bundle /usr/local/bundle
COPY --from=builder --chown=rails:rails /app /app

ENV RAILS_ENV=production \
    RAILS_SERVE_STATIC_FILES=true \
    RAILS_LOG_TO_STDOUT=true

EXPOSE 3000

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]