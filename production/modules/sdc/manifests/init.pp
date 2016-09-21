class sdc {

  Exec  { environment => [ "MDM_IP=10.136.220.40,10.136.220.41i" ] }
 
  package { 'sdc':
    provider => 'rpm',
    ensure => 'present',
    source => '/root/scaleio/sdc.rpm',
 }
}




