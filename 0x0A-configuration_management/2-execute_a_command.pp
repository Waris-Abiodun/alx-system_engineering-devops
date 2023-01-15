# executing a comand to kil a process looping indefinetyly

exec{'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
