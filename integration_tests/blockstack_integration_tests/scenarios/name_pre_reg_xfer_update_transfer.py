#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Blockstack
    ~~~~~
    copyright: (c) 2014-2015 by Halfmoon Labs, Inc.
    copyright: (c) 2016 by Blockstack.org

    This file is part of Blockstack

    Blockstack is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Blockstack is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with Blockstack. If not, see <http://www.gnu.org/licenses/>.
""" 

import testlib
import pybitcoin
import json

wallets = [
    testlib.Wallet( "5JesPiN68qt44Hc2nT8qmyZ1JDwHebfoh9KQ52Lazb1m1LaKNj9", 100000000000 ),
    testlib.Wallet( "5KHqsiU9qa77frZb6hQy9ocV7Sus9RWJcQGYYBJJBb2Efj1o77e", 100000000000 ),
    testlib.Wallet( "5Kg5kJbQHvk1B64rJniEmgbD83FpZpbw2RjdAZEzTefs9ihN3Bz", 100000000000 ),
    testlib.Wallet( "5JuVsoS9NauksSkqEjbUZxWwgGDQbMwPsEfoRBSpLpgDX1RtLX7", 100000000000 ),
    testlib.Wallet( "5KEpiSRr1BrT8vRD7LKGCEmudokTh1iMHbiThMQpLdwBwhDJB1T", 100000000000 ),
    testlib.Wallet( "5K9LmMQskQ9jP1p7dyieLDAeB6vsAj4GK8dmGNJAXS1qHDqnWhP", 100000000000 ),
    testlib.Wallet( "5KcNen67ERBuvz2f649t9F2o1ddTjC5pVUEqcMtbxNgHqgxG2gZ", 100000000000 )
]

debug = False
consensus = "17ac43c1d8549c3181b200f1bf97eb7d"

def scenario( wallets, **kw ):

    global debug, consensus

    resp = testlib.blockstack_namespace_preorder( "test", wallets[1].addr, wallets[0].privkey )
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_namespace_reveal( "test", wallets[1].addr, 52595, 250, 4, [6,5,4,3,2,1,0,0,0,0,0,0,0,0,0,0], 10, 10, wallets[0].privkey )
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_namespace_ready( "test", wallets[1].privkey )
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_preorder( "foo.test", wallets[2].privkey, wallets[3].addr )
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )
    
    resp = testlib.blockstack_name_register( "foo.test", wallets[2].privkey, wallets[3].addr )
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    # ping-ping a bit... 3 --> 4 --> 5 --> 4 --> 5 --> 4
    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[3].privkey, safety_checks=False ) 
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey, safety_checks=False )
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    # update (4)
    resp = testlib.blockstack_name_update( "foo.test", "11" * 20, wallets[4].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    # ping-ping a bit... 4 --> 5 --> 4 --> 5 --> 4 --> 5
    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )
    
    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey, safety_checks=False)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    # now update (5)
    resp = testlib.blockstack_name_update( "foo.test", "22" * 20, wallets[5].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_update( "foo.test", "33" * 20, wallets[4].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_update( "foo.test", "44" * 20, wallets[4].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_update( "foo.test", "55" * 20, wallets[4].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_update( "foo.test", "66" * 20, wallets[4].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )
 
    resp = testlib.blockstack_name_transfer( "foo.test", wallets[5].addr, True, wallets[4].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )

    resp = testlib.blockstack_name_update( "foo.test", "11" * 20, wallets[5].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    consensus = testlib.get_consensus_at( testlib.get_current_block(**kw), **kw )
    testlib.next_block( **kw )

    resp = testlib.blockstack_name_transfer( "foo.test", wallets[4].addr, True, wallets[5].privkey)
    if debug or 'error' in resp:
        print json.dumps( resp, indent=4 )

    testlib.next_block( **kw )



def check( state_engine ):

    global consensus

    # not revealed, but ready 
    ns = state_engine.get_namespace_reveal( "test" )
    if ns is not None:
        print "'test' not revealed"
        return False 

    ns = state_engine.get_namespace( "test" )
    if ns is None:
        print "'test' not found"
        return False 

    if ns['namespace_id'] != 'test':
        print "'test' not returned"
        return False 

    # not preordered
    preorder = state_engine.get_name_preorder( "foo.test", pybitcoin.make_pay_to_address_script(wallets[2].addr), wallets[3].addr )
    if preorder is not None:
        print "'foo.test' still preordered"
        return False
    
    # registered 
    name_rec = state_engine.get_name( "foo.test" )
    if name_rec is None:
        print "'foo.test' not registered"
        return False 

    # updated, and data is preserved
    if name_rec['value_hash'] != '11' * 20:
        print "'foo.test' invalid value hash"
        return False 

    # transferred 
    if name_rec['address'] != wallets[4].addr or name_rec['sender'] != pybitcoin.make_pay_to_address_script(wallets[4].addr):
        print "'foo.test' invalid owner"
        return False 

    # consensus from last NAME_UPDATE 
    if name_rec['consensus_hash'] != consensus:
        print "quirk not preserved: consensus hash %s != %s" % (name_rec['consensus_hash'], consensus)
        return False

    return True
