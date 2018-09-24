provider "aws" {
  region     = "us-west-2"
  access_key = "AKIAICATSZH6N3V5NWKQ"
  secret_key = "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"
}

variable "name" {
  default = "aws-dev"
}

variable "enc_key" {
  default = "arn:aws:kms:us-west-2:378420603465:key/34343d60-6e24-4e26-82df-7cfa98b8d7c8"
}

variable "vpc_cidr" {
  default = "10.26.32.0/19"
}

resource "aws_s3_bucket" "oag_bucket" {
  bucket = "sfo-dev-kinesis-oag"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "AES256"
      }
    }
  }
}

resource "aws_kinesis_stream" "oag_schedflights" {
  name             = "${var.name}-oag-schedflights"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

data "aws_iam_policy_document" "fh_role" {
  statement {
    sid = "1"
    effect = "Allow"
    actions = [
      "sts:AssumeRole"
    ]
    principals {
      type        = "Service"
      identifiers = ["firehose.amazonaws.com"]
    }
  }
  statement {
    sid = "2"
    effect = "Allow"
    actions = [
      "kinesis:DescribeStream",
      "kinesis:GetShardIterator",
      "kinesis:GetRecords"
    ]
    resources = ["arn:aws:kinesis:us-west-2:378420603465:stream/*"],
  }
}

resource "aws_iam_role" "oag_fh_role" {
  name = "${var.name}-oag"
  assume_role_policy = "${data.aws_iam_policy_document.fh_role.json}"
}

resource "aws_kinesis_firehose_delivery_stream" "oag_fh" {
  name        = "${var.name}-oag-schedflights"
  destination = "s3"
  s3_configuration {
    role_arn   = "${aws_iam_role.oag_fh_role.arn}"
    bucket_arn = "${aws_s3_bucket.oag_bucket.arn}"
    buffer_size        = 128
    buffer_interval    = 900
    compression_format = "GZIP"
    kms_key_arn = "${var.enc_key}"
  }
  kinesis_source_configuration {
    kinesis_stream_arn = "${aws_kinesis_stream.oag_schedflights.arn}"
    role_arn = "${aws_iam_role.oag_fh_role.arn}"
  }
}

resource "aws_s3_bucket" "fs_bucket" {
  bucket = "sfo-dev-kinesis-fs"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "AES256"
      }
    }
  }
}

resource "aws_kinesis_stream" "fs-flightstatus" {
  name             = "${var.name}-fs-flightstatus"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

resource "aws_kinesis_stream" "fs-appendix" {
  name             = "${var.name}-fs-appendix"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

resource "aws_kinesis_stream" "fs-fids" {
  name             = "${var.name}-fs-fids"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

resource "aws_kinesis_stream" "fs-delayindex" {
  name             = "${var.name}-fs-delayindex"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

resource "aws_kinesis_stream" "fs-weather" {
  name             = "${var.name}-fs-weather"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

resource "aws_kinesis_stream" "fs-schedflights" {
  name             = "${var.name}-fs-schedflights"
  shard_count      = 1
  retention_period = 24
  encryption_type = "KMS"
  kms_key_id = "${var.enc_key}"

  tags{
    Domains = "PSS-EDL-PAS"
    Other = "ONECLOUD-FLOW MANAGEMENT"
  }
}

resource "aws_s3_bucket" "dot_bucket" {
  bucket = "sfo-dev-kinesis-dot"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm     = "AES256"
      }
    }
  }
}