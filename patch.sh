#!/bin/sh
#kubectl casskop cleanup --pod cassandra-cluster-dc1-rack1-0
kubectl patch CassandraCluster cassandra-cluster --type=json -p='[{"op": "replace", "path": "/spec/topology/dc/0/nodesPerRacks", "value": 0}]'
#kubectl patch CassandraCluster cassandra-cluster --type=json -p='[{"op": "remove", "path": "/spec/topology/dc/2"}]'
