FROM golang:1.22-alpine AS builder

WORKDIR /app

COPY . .

RUN go build main.go

FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/main .

ENTRYPOINT ["./main"]

