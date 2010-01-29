module RDF::Turtle
  ##
  # Turtle parser.
  # FIXME doc me up
  class Reader < RDF::Reader
    format RDF::Turtle::Format
 
    ##
    # @return [Array, nil]
    # # FIXME docs
    def read_triple
      raise NotImplementedError
      loop do
        readline.strip! # EOFError thrown on end of input
 
        unless blank? || read_comment
          subject = read_uriref || read_bnode || fail_subject
          predicate = read_uriref || fail_predicate
          object = read_uriref || read_bnode || read_literal || fail_object
          return [subject, predicate, object]
        end
      end
    end
 
  end
end
 

