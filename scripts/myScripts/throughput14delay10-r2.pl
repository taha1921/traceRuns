#!/usr/bin/perl -w

use strict;
use LWP::UserAgent;
use HTTP::Request::Common;

my $receiver_pid = fork;

if ( $receiver_pid < 0 ) {
  die qq{$!};
} elsif ( $receiver_pid == 0 ) {
  # child
  exec q{verus-r2/src/verus_server -name test -p 60001 -t 1000} or die qq{$!};
}

chomp( my $prefix = qx{dirname `which mm-link`} );
my $tracedir = $prefix . q{mahimahi/traces};

my @command = qw{mm-delay 35 mm-link UPLINK DOWNLINK};

# display livegraphs if we seem to be running under X
if ( defined $ENV{ 'DISPLAY' } ) {
    push @command, qw{--meter-downlink --meter-downlink-delay};
}

push @command, qw{ --uplink-queue=red --downlink-queue=red --uplink-queue-args=min_bytes=375000max_bytes=1125000drop_percentage=10 --downlink-queue-args=min_bytes=375000max_bytes=1125000drop_percentage=10 --once --downlink-log=logs/throughput14Delay10_log_r2 -- sh -c};

push @command, q{verus-r2/src/verus_client $MAHIMAHI_BASE -p 60001};

die unless $command[ 3 ] eq "UPLINK";
$command[ 3 ] = qq{traces/myTraces/16.667000-uplink-14.001207-0.010000.dat.out};

die unless $command[ 4 ] eq "DOWNLINK";
$command[ 4 ] = qq{traces/myTraces/16.667000-downlink-14.001207-0.010000.dat.out};

system @command;

# kill the receiver
kill 'INT', $receiver_pid;

print "\n";

# analyze performance locally
system q{mm-throughput-graph 500 logs/throughput14Delay10_log_r2 > /dev/null};

print "\n";
